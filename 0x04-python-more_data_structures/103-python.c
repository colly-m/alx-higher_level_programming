#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * print_python_list - function to check if a Python object is a list
 * @p: pointer to the object list
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	if (PyList_CHeck(p))
	{
		Py_ssize_t size = ((PyVarObject *)p)->ob_size;
		Py_ssize_t s;

		printf("[*] Python list info\n");
		printf("Size of the python List = %ld\n", size);
		printf("Allocated =  %ld\n", ((PyListObject *)p)->allocated);

		for (s = 0; s < size; s++)
		{
			printf("Element %ld: %s\n", s, Py_TYPE(PyList_GetItem(p, s))->tp_name);
		}
	}
	else
	{
		PyErr_SetString(PyExc_TypeError, "Object is not a list");
	}
}

/**
 * print_python_bytes - function to check if a python object is a byte
 * @p: pointer to the object list
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = ((PyVarObject *)p)->ob_size;
	Py_ssize_t u;
	char *str = ((PyBytesObject *)p)->ob_sval;

	if (PyBytes_Check(p))
	{
		printf("[.] bytes object info\n";
		printf("Size: %ld\n", size);
		printf("Trying string: %s\n", str);

		printf("first %ld bytes: ", size < 10 ? size : 10);
		for (u = 0; u < size && u < 10; u++)
		{
			printf("%02x", str[u] & 0xff);
			if (u < 9 && u < size - 1)
			printf(" ");
		}
		printf("\n");
	}
	else
	{
		PyErr_SetString(PyExc_TypeError, "Object is not a bytes object");
	}
}
