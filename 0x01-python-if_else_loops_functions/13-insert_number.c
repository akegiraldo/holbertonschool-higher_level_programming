#include "lists.h"

/**
 * insert_node - entry point
 * @head: listint_t variable
 * @number: int variable
 * Return: 
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *aux;
	int i = 0;

	if (head == NULL)
		return (NULL);
	aux = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		if (number < aux->n)
		{
			new->next = aux;
			*head = new;
			i = 1;
		}
		else
		{
			while (aux->next != NULL)
			{
				if (number < aux->next->n)
				{
					new->next = aux->next;
					aux->next = new;
					break;
				}
				aux = aux->next;
			}
		}
		if (aux->next == NULL && i == 0)
			aux->next = new, new->next = NULL;
	}
	return (new);
}
