#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// This is a combination of header and body files for the
// sorting algorithms used for this project.
//
// Featured in this file are the following algorithms:
//
// 	1. BozoSort
// 	   Randomly swap two elements of array
// 	2. QuickSort
// 	   Very famous computer sorting algorithm
// 
// To compile this file, use this command:
// 	gcc -shared -o sort_algs.so -fPIC sort_algs.c

// Swap two integers in an array
void swap(int *arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

// Check if the array is sorted
int isSorted(int *arr, int n) {
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i - 1]) {
            return 0;
        }
    }
    return 1;
}

// Bozosort algorithm
void bozosort(int *arr, int n) {
    srand(time(NULL)); // Initialize random seed

    while (!isSorted(arr, n)) {
        // Randomly select two indices to swap
        int i = rand() % n;
        int j = rand() % n;

        // Swap the elements at indices i and j
        swap(arr, i, j);
    }
}

// Partition the array and return the pivot index
int partition(int *arr, int low, int high) {
    int pivot = arr[high]; // Choose the rightmost element as the pivot
    int i = (low - 1);     // Index of smaller element

    for (int j = low; j <= high - 1; j++) {
        // If the current element is smaller than or equal to the pivot
        if (arr[j] <= pivot) {
            i++; // Increment index of smaller element
            swap(arr, i, j);
        }
    }
    swap(arr, i + 1, high);
    return (i + 1);
}

// Quicksort algorithm
void quicksort(int *arr, int low, int high) {
    if (low < high) {
        // Partition the array and get the pivot index
        int pivotIndex = partition(arr, low, high);

        // Recursively sort elements before and after the pivot
        quicksort(arr, low, pivotIndex - 1);
        quicksort(arr, pivotIndex + 1, high);
    }
}

void quickSortArray(int *arr, int length) {
    quicksort(arr, 0, length - 1);
}

void slowSort(int arr[], int size) {
    // The function now operates on the globally defined or dynamically allocated array.
    // You can access it as arr[0], arr[1], ..., arr[size - 1].

    // Base case: If the array has one or zero elements, it's already sorted.
    if (size <= 1) {
        return;
    }

    int mid = size / 2;

    // Recursively sort the two halves
    slowSort(arr, mid);
    slowSort(arr + mid, size - mid);

    // If the last element of the first half is greater than the first element of the second half,
    // swap them to maintain sorting order.
    if (arr[mid - 1] > arr[mid]) {
        int temp = arr[mid - 1];
        arr[mid - 1] = arr[mid];
        arr[mid] = temp;
    }
}