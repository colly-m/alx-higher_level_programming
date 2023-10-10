#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function to print info on python list
 * @p: pointer to object to be checked
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	long int size = PyList_size(p);
	int t;
	PyListObject *ob = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", ob->allocated);

	for (t = 0; t < Py_SIZE(p); t++)
		printf("Element %d: %s\n", t, Py_TYPE(ob_GetItem[t])->tp_name);
}
