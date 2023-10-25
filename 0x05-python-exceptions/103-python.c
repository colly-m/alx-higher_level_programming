#include <Python.h>
#include <stdio.h>
#include <floatobject.h>
#include <stdlib.h>
#include <object.h>
#include <string.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_list - function to print a python list
 * @p: pointer to what to be printed
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t s = PyList_Size(p);
	Py_ssize_t z;

	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", s);
		printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

		for (z = 0; z < s; z++)
		{
			PyObject *item = PyList_GetItem(p, z);
			printf("Element %ld: %s\n", z, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		printf(" [ERROR] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - function to print python bytes
 * @p: pointer to what to print
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t s = PyBytes_Size(p);
	Py_ssize_t z;
	char *str = PyBytes_AsString(p);

	if (PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf(" size:%ld\n", s);
		printf(" trying string: %s\n", str);
		printf(" first 10 bytes: ");

		for (z = 0; z < s && z < 10; z++)
		{
			printf("%02x", (unsigned char)str[z]);
			if (z < s - 1)
			{
				printf(" ");
			}
		}
		printf("\n");
	}
	else
	{
		printf(" [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - function to print python float objects
 * @p: pointer to what to print
 * Return: void
 */
void print_python_float(PyObject *p)
{
	double val = PyFloat_AS_DOUBLE(p);

	if (PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf(" value: %f\n", val);
	}
	else
	{
		printf(" [ERROR] Invalid Float Object\n");
	}
}
