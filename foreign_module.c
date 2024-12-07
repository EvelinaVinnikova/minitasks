#include <Python.h>

static PyObject* matrix_multiply(PyObject *matrix1, PyObject *matrix2) {
    Py_ssize_t n = PyList_Size(matrix1);
    PyObject *result = PyList_New(n);

    for (Py_ssize_t i = 0; i < n; i++) {
        PyObject *row = PyList_New(n);
        for (Py_ssize_t j = 0; j < n; j++) {
            double sum = 0.0;
            for (Py_ssize_t k = 0; k < n; k++) {
                PyObject *m1_val = PyList_GetItem(PyList_GetItem(matrix1, i), k);
                PyObject *m2_val = PyList_GetItem(PyList_GetItem(matrix2, k), j);
                sum += PyFloat_AsDouble(m1_val) * PyFloat_AsDouble(m2_val);
            }
            PyList_SetItem(row, j, PyFloat_FromDouble(sum));
        }
        PyList_SetItem(result, i, row);
    }
    return result;
}

static PyObject* foreign_matrix_power(PyObject *self, PyObject *args) {
    PyObject *matrix;
    int power;

    if (!PyArg_ParseTuple(args, "Oi", &matrix, &power)) {
        return NULL;
    }

    if (power < 1) {
        PyErr_SetString(PyExc_ValueError, "Power must be a positive integer");
        return NULL;
    }

    Py_ssize_t n = PyList_Size(matrix);
    for (Py_ssize_t i = 0; i < n; i++) {
        if (PyList_Size(PyList_GetItem(matrix, i)) != n) {
            PyErr_SetString(PyExc_ValueError, "Matrix must be square");
            return NULL;
        }
    }


    PyObject *result = matrix;
    Py_INCREF(result);


    for (int i = 1; i < power; i++) {
        PyObject *temp = result;
        result = matrix_multiply(temp, matrix);
        Py_DECREF(temp);
    }

    return result;
}

static PyMethodDef ForeignMethods[] = {
    {"foreign_matrix_power", foreign_matrix_power, METH_VARARGS,
     "Raise a square matrix to a positive integer power"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef foreignmodule = {
    PyModuleDef_HEAD_INIT,
    "foreign",
    NULL,
    -1,
    ForeignMethods
};

PyMODINIT_FUNC PyInit_foreign(void) {
    return PyModule_Create(&foreignmodule);
}