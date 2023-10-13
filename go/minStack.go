// https://leetcode.com/problems/min-stack

package leetcode

type MinStack struct {
	stack []minStack
}

type minStack struct {
	val int
	min int
}

func Constructor() MinStack {
	return MinStack{}
}

func (ms *MinStack) Push(val int) {
	var min int
	ssize := len(ms.stack)
	if ssize == 0 {
		min = val
	} else {
		min = ms.stack[ssize-1].min
	}
	if val < min {
		min = val
	}
	ms.stack = append(ms.stack, minStack{val, min})
}

func (ms *MinStack) Pop() {
	ssize := len(ms.stack)
	ms.stack = ms.stack[:ssize-1]
}

func (ms *MinStack) Top() int {
	ssize := len(ms.stack)
	return ms.stack[ssize-1].val
}

func (ms *MinStack) GetMin() int {
	ssize := len(ms.stack)
	return ms.stack[ssize-1].min
}

/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
