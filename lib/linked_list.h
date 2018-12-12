

typedef struct {
    int *val;
    void *next;
} element_t;

element_t * new_element(void);

element_t * new_list(void);

void append_val(element_t *list, int val);

element_t *get_element_indexed(element_t * list, int index);

