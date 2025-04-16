#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX(A, B) (A > B ? A : B)

static PyObject *shortcuts_gcd(PyObject *self, PyObject *args);
static PyObject *shortcuts_lcs(PyObject *self, PyObject *args);

static int __gcd(int a, int b);
static int __lcs(char* s1, char* s2, int l1, int l2);

static PyMethodDef ShortcutMethods [] = {
	{"gcd", shortcuts_gcd, METH_VARARGS, "Compute Greatest Common Divisor" },
	{"lcs", shortcuts_lcs, METH_VARARGS, "Longest Common Subsequence" }
};

PyMODINIT_FUNC initshortcuts(void)
{
    (void) Py_InitModule("shortcuts", ShortcutMethods);
}

static PyObject *shortcuts_gcd(PyObject *self, PyObject *args)
{
    int a, b, result;
    if(!PyArg_ParseTuple(args, "ii", &a, &b))
    {
        return NULL;
    }

    result = __gcd(a, b);
	return Py_BuildValue("i", result);
}

static PyObject *shortcuts_lcs(PyObject *self, PyObject *args)
{
    char* s1;
    char* s2;
    int result;

    if(!PyArg_ParseTuple(args, "ss", &s1, &s2))
    {
        return NULL;
    }

    result = __lcs(s1, s2, strlen(s1), strlen(s2));
    return Py_BuildValue("i", result);
}

static int __gcd(int a, int b)
{
    if(b == 0) return a;
    return __gcd(b, a % b);
}

static int __lcs(char* s1, char* s2, int l1, int l2)
{
    int i, j;
    int matrix[100][100];
    int result;

    memset(matrix, 0, sizeof(matrix));

    for(i = 1; i<=l1; i++)
    {
        for(j = 1; j<=l2; j++)
        {
            if(s1[i-1] == s2[j-1])
            {
                matrix[i][j] = matrix[i-1][j-1] + 1;
            }
            else
            {
                matrix[i][j] = MAX(matrix[i][j-1], matrix[i-1][j]);
            }
        }
    }
    return matrix[l1][l2];
}