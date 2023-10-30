// https://leetcode.com/problems/kth-largest-element-in-a-stream

package KthLargest

import "container/heap"

type KthLargest struct {
	k    int
	heap *IntHeap
}

func Constructor(k int, nums []int) KthLargest {
	h := &IntHeap{}
	heap.Init(h)

	kthl := KthLargest{
		k:    k,
		heap: h,
	}

	for _, num := range nums {
		kthl.Add(num)
	}

	return kthl
}

func (kthl *KthLargest) Add(val int) int {
	heap.Push(kthl.heap, val)
	if len((*kthl.heap)) > kthl.k {
		heap.Pop(kthl.heap)
	}
	return kthl.heap.Peek()
}

// An IntHeap is a min-heap of ints.
// https://pkg.go.dev/container/heap
type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}

func (h IntHeap) Less(i, j int) bool {
	return h[i] < h[j]
}

func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}

func (h *IntHeap) Push(x any) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func (h *IntHeap) Peek() int {
	return (*h)[0]
}
