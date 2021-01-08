# This program generates all sublists of a given list.
# Created By: AJ Singh
# Date: Jan 7, 2021


# Compute all sublists of a given list.
# @param my_list: The list in question.
# @return: List containing all sublists.
def all_sublists(my_list: list) -> list:
    """Generates list of all sublists."""

    sublists = [[]]

    length = 1
    while length <= len(my_list):
        for k in range(len(my_list)-length+1):
            sublist = my_list[k:k+length]
            sublists.append(sublist)

        length += 1

    return sublists


def main():
    l = list(input("Enter a list: ").split())
    sublists = all_sublists(l)

    print("\nThe sublists are:")
    for _ in sublists:
        print(_)


if __name__ == '__main__':
    main()
