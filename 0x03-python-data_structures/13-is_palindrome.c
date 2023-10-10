#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - function to reverse a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prv = NULL;

	while (node)
	{
		next = node->next;
		node->next = prv;
		prv = node;
		node = next;
	}

	*head = prv;
	return (*head);
}

/**
 * is_palindrome - function to check if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: linked list is not a palindrome 0, linked list is a palindrome 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *rev, *mid;
	size_t size = 0, s;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (s = 0; s < (size / 2) - 1; s++)
		temp = temp->next;

	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);

	temp = temp->next->next;
	rev = reverse_listint(&temp);
	mid = rev;

	temp = *head;
	while (rev)
	{
		if (temp->n != rev->n)
			return (0);
		temp = temp->next;
		rev = rev->next;
	}
	reverse_listint(&mid);

	return (1);
}
