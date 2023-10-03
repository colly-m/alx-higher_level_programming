#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function to insert node in sorted linked list
 * @head: pointer to first node of linked list
 * @number: pointer to number to insert
 * Return: address of the new node, or NULL (failed)
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nw;
	listint_t *cur = *head;

	if (!head)
		return NULL;

	nw = malloc(sizeof(listint_t));
	if (!nw)
		return (NULL);

	nw->n = number;
	nw->next = NULL;

	if (*head == NULL)
		*head = nw;
	else if (number < cur->n)
	{
		nw->next = cur;
		*head = nw;
	}
	else
	{
		while (cur->next)
		{
			if (number > cur->next->n)
				cur = cur->next;
			else
				break;
		}
		nw->next = cur->next;
		cur->next = nw;
	}

	return (nw);
}
