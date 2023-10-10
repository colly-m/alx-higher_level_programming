#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - function to print info on python list
 * @p: pointer to object list to be check
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *ob;
	int s, t, u;

	s = Py_SIZE(p);
	t - ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", t);

	for (u = 0; u < s; u++)
	{
		printf("Element %d: ", u);

		ob = PyList_GetItem(p, u);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
