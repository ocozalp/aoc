package com.ocozalp.ai.common;

import java.util.ArrayList;
import java.util.Hashtable;

/**
 * Created by ocozalp on 5/18/14.
 *
 * General class for non-deterministic problems
 *
 */
public class Problem {

    private ArrayList<State> states;
    private Hashtable<State, Hashtable<Action, ArrayList<State>>> transitionTable;
    private ArrayList<State> goalStates;

    public Problem() {
        this.states = new ArrayList<State>();
        this.transitionTable = new Hashtable<State, Hashtable<Action, ArrayList<State>>>();
        this.goalStates = new ArrayList<State>();
    }

    public void addState(State state) {
        if(!states.contains(state)) {
            states.add(state);
            transitionTable.put(state, new Hashtable<Action, ArrayList<State>>());
        }
    }

    public void addActionResult(State currentState, Action action, State resultState) {
        addState(currentState);
        addState(resultState);

        Hashtable<Action, ArrayList<State>> stateTransitionTable = this.transitionTable.get(currentState);
        if(!stateTransitionTable.containsKey(action)) {
            stateTransitionTable.put(action, new ArrayList<State>());
        }

        if(!stateTransitionTable.get(action).contains(resultState)) {
            stateTransitionTable.get(action).add(resultState);
        }
    }

    public ArrayList<Action> getActionsOfState(State state) {
        ArrayList<Action> result = new ArrayList<Action>();

        Hashtable<Action, ArrayList<State>> stateTransitionTable = this.transitionTable.get(state);

        if(stateTransitionTable != null) {
            for(Action action : stateTransitionTable.keySet()) {
                result.add(action);
            }
        }

        return result;
    }

    public ArrayList<State> getResultsOfAction(State state, Action action) {
        Hashtable<Action, ArrayList<State>> stateTransitionTable = this.transitionTable.get(state);

        if(stateTransitionTable != null && stateTransitionTable.get(action) != null) {
            return stateTransitionTable.get(action);
        }

        return new ArrayList<State>();
    }

    public void addGoalState(State state) {
        if(!goalStates.contains(state)) {
            goalStates.add(state);
        }
    }

    public boolean isGoalState(State state) {
        return goalStates.contains(state);
    }
}
