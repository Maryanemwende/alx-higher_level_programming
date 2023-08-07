#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *behind, *ahead;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	behind = list->next;
	ahead = list->next->next;

	while (behind && ahead && ahead->next)
	{
		if (behind == ahead)
		{
			return (1);
		}
		behind = behind->next;
		ahead = ahead->next->next;
	}
	return (0);
}
