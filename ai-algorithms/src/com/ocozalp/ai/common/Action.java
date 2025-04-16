package com.ocozalp.ai.common;

/**
 * Created by ocozalp on 5/18/14.
 */
public class Action {
    private String name;

    public Action(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    @Override
    public boolean equals(Object obj) {
        return (obj instanceof Action) && this.name.equals(((Action) obj).name);
    }

    @Override
    public int hashCode() {
        return this.name.hashCode();
    }
}
