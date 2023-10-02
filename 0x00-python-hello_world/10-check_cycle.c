#include "lists.h"

/**
 * check_cycle - function to check if a singly linked list has
 * a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *sec = list;
	listint_t *fir = list;

	if (!list)
		return (0);

	while (sec && fir && fir->next)
	{
		sec = sec->next;
		fir = fir->next->next;

		if (sec == fir)
			return (1);
	}
	return (0);
}
