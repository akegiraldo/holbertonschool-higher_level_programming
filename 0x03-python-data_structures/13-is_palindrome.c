#include "lists.h"

/**
 * is_palindrome - entry point
 * @head: listint variable
 *
 * Return: int variable
*/

int is_palindrome(listint_t **head)
{
	int vector[1000000], i = 0, j = 0, t = 0;
	listint_t *tmp;

	if (head == NULL || (*head) == NULL)
		return (1);
	tmp = *head;
	while (tmp)
		vector[i] = tmp->n, i++, tmp = tmp->next;
	i--;
	if (i % 2 != 0)
		t = (i + 1) / 2;
	else
		t = i / 2;
	while (j < t)
	{
		if (vector[j] != vector[i])
			return (0);
		i--;
		j++;
	}
	return (1);
}
