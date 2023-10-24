// https://leetcode.com/problems/lru-cache

package LRUCache

import "container/list"

type Node struct {
	key int
	val int
}

type LRUCache struct {
	cache    map[int]*list.Element
	capacity int
	list     *list.List
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		cache:    make(map[int]*list.Element, capacity),
		capacity: capacity,
		list:     list.New(),
	}
}

func (lru *LRUCache) Get(key int) int {
	if elem, ok := lru.cache[key]; ok {
		lru.list.MoveToBack(elem)
		return elem.Value.(Node).val
	}
	return -1
}

func (lru *LRUCache) Put(key int, value int) {
	if elem, ok := lru.cache[key]; ok {
		lru.list.Remove(elem)
	}

	elem := lru.list.PushBack(Node{key, value})
	lru.cache[key] = elem

	if len(lru.cache) > lru.capacity {
		elem := lru.list.Front()
		node := lru.list.Remove(elem)
		delete(lru.cache, node.(Node).key)
	}
}
