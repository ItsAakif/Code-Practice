#include "queue.h"
#include <assert.h>
#include <stdlib.h>

/* Full definition of the queue structure */
typedef struct s_internalQueue {
	void *value;
	struct s_internalQueue *next;
} InternalQueue;

struct s_queue{
	InternalQueue *head;
	InternalQueue *tail;
	unsigned int size;
};

Queue *createQueue(){
	Queue *q = malloc(sizeof(Queue));
	q->head = q->tail = NULL;
	q->size = 0;
	return(q);
}

void deleteQueue(ptrQueue *q) {
	InternalQueue *toDelete = (*q)->head;
	while (toDelete) {
		InternalQueue *f = toDelete;
		toDelete = toDelete->next;
		free (f);
	}
	free(*q);
	*q = NULL;
}

Queue *queuePush(Queue *q, void *v){
	InternalQueue **insert_at = (q->size ? &(q->tail->next) : &(q->head));
	InternalQueue *new = malloc(sizeof(InternalQueue));
	new->value = v;
	new->next = NULL;
	*insert_at = new;
	q->tail = new;
	++(q->size);
	return (q);
}

Queue *queuePop(Queue *q){
	assert (!queueEmpty(q));
	InternalQueue *old = q->head;
	q->head = q->head->next;
	q->size--;
	free (old);
	return (q);
}

void *queueTop(Queue *q){
	assert (!queueEmpty(q));
	return (q->head->value);
}

bool queueEmpty(Queue *q){
	return (q->size == 0);
}

unsigned int queueSize(Queue *q) {
	return q->size;
}

void queueDump(FILE *f, Queue *q, void(*dumpfunction)(FILE *f, void *e)) {
	fprintf(f, "(%d) --  ", q->size);
	for (InternalQueue *c=q->head; c != NULL; c = c->next)
		dumpfunction(f, c->value);
}
