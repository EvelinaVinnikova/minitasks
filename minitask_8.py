def format_table(benchmarks, algos, results):
    col_widths = [max(len("Benchmark"), max(len(b) for b in benchmarks))]
    col_widths += [max(len(algo), max(len(f"{result:.2f}") for result in col)) for algo, col in zip(algos, zip(*results))]

    header = "| " + " | ".join([f"{'Benchmark':<{col_widths[0]}}"] +
                                [f"{algo:<{col_widths[i + 1]}}" for i, algo in enumerate(algos)]) + " |"
    separator = "|-" + "-|-".join("-" * width for width in col_widths) + "-|"

    output = [header, separator]

    for benchmark, row in zip(benchmarks, results):
        row_data = [f"{benchmark:<{col_widths[0]}}"] + [f"{value:<{col_widths[i + 1]}.2f}" for i, value in enumerate(row)]
        output.append("| " + " | ".join(row_data) + " |")

    print("\n".join(output))
    return output


format_table(["best case", "worst case"], ["quick sort", "merge sort", "bubble sort"], [[1.23, 1.56, 2.0], [3.3, 2.9, 3.9]])
