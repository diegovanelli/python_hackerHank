# You are given  queries. Each query is of the form two integers described below:
# - 1 : x Insert x in your data structure.
# - 2 : y Delete one occurence of y from your data structure, if present.
# - 3 : z Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

# The queries are given in the form of a 2-D array queries of size q where queries[i][0] contains the operation, and queries[i][1] contains the data element.

# Example

# queries = [(1,1), (2,2), (3,2), (1,1), (1,1), (2,1), (3,2)]

# return an array with the output: [0, 1]
def freqQuery(queries):
    element_freq = {}
    freq_count = {}
    result = []

    for query in queries:
        operation = query[0]
        value = query[1]

        if operation == 1:
            if value in element_freq:
                if element_freq[value] in freq_count:
                    freq_count[element_freq[value]] -= 1
                element_freq[value] += 1
            else:
                element_freq[value] = 1

            if element_freq[value] in freq_count:
                freq_count[element_freq[value]] += 1
            else:
                freq_count[element_freq[value]] = 1

        elif operation == 2:
            if value in element_freq and element_freq[value] > 0:
                freq_count[element_freq[value]] -= 1
                element_freq[value] -= 1
                freq_count[element_freq[value]] += 1

        elif operation == 3:
            if value in freq_count and freq_count[value] > 0:
                result.append(1)
            else:
                result.append(0)

    return result


