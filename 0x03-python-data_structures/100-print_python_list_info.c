#include <Python.h>

/**
 * print_python_list_info - function to print info on python list
 * @p: pointer to object list to be check
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *ob;
	Py_ssize_t s, t, u;

	s = Py_SIZE(p);
	t - ((PyListObject *)p)->t;

	printf("[*] Size of the Python List = %ld\n", s);
	printf("[*] Allocated = %ld\n", t);

	for (u = 0; u < s; u++)
	{
		printf("Element %ld: ", u);

		ob = PyList_GetItem(p, u);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
