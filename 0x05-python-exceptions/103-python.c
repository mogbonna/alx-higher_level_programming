#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p)
{
	long int size = PyList_size(p);
	int i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	const char *bytes;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	bytes = PyBytes_AsString(p);

	printf("[.] Size: %ld\n", size);
	printf("[.] trying string: %s\n", bytes);
	printf("  first 10 bytes:");

	if (size < 10)
	{
		for (i = 0; i < size; i++)
		{
			printf(" %02x", bytes[i] & 0xff);
		}
	}
	else
	{
		for (i = 0; i < 10; i++)
		{
			printf(" %02x", bytes[i] & 0xff);
		}
	}

	printf("\n");
}

void print_python_float(PyObject *p)
{
	char *repr;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "  [ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float info\n");

	if (PyFloat_IS_INFINITY(p))
	{
		printf("  value: %s\n", PyFloat_AS_STRING(p));
	}
	else
	{
		repr = PyOS_double_to_string
			(PyFloat_AS_DOUBLE(p), 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", repr);
	}
}
