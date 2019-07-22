package com.aruba.qoeapp.common;

import java.util.LinkedHashMap;

class LRUCache {

    private LinkedHashMap<Integer, Integer> lhm = new LinkedHashMap<Integer, Integer>();
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
    }

    public int get(int key) {
        if (this.lhm.containsKey(key)) {
            int ret = lhm.get(key);
            lhm.remove(key);
            lhm.put(key, ret);
            return ret;
        } else {
            return -1;
        }
    }

    public void put(int key, int value) {
        lhm.remove(key);
        lhm.put(key, value);
        if (lhm.size() > this.capacity) {
            Integer krm = null;
            for (Integer k : lhm.keySet()) {
                krm = k;
                break;
            }
            lhm.remove(krm);
        }
    }
}