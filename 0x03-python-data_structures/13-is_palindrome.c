#include "lists.h"

/**
 * is_palindrome - checks whether a list is a palindrome
 * @head: address of the pointer to the list
 *
 * Return: 1 if it's a palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *fol = NULL, *adv = NULL;
	int fol_node, adv_node, count;

	if (!(*head) || !((*head)->next))
		return (1);
	fol = (*head)->next;
	adv = fol;
	fol_node = adv_node = 2;
	while (adv->next)
	{
		adv = adv->next;
		adv_node++;
	}
	if ((*head)->n != adv->n)
		return (0);
	while (fol != adv && fol->next != adv)
	{
		adv_node--;
		adv = fol->next;
		count = fol_node + 1;
		while (count < adv_node)
		{
			adv = adv->next;
			count++;
		}
		if (fol->n != adv->n)
			return (0);
		fol = fol->next;
		fol_node++;
	}
	return (1);
}
