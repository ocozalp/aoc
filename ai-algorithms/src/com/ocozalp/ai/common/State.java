package com.ocozalp.ai.common;

/**
 * Created by ocozalp on 5/18/14.
 */
public class State {
    private int id;

    public State(int id) {
        this.id = id;
    }

    public int getId() {
        return this.id;
    }

    @Override
    public boolean equals(Object obj) {
        if(!(obj instanceof State)) return false;

        State target = (State) obj;

        return this.id == target.id;
    }

    @Override
    public int hashCode() {
        return this.id * 997;
    }
}
