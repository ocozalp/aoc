package com.ocozalp.ai.search;

import com.ocozalp.ai.common.Action;
import com.ocozalp.ai.common.Problem;
import com.ocozalp.ai.common.State;

/**
 * Created by ocozalp on 5/18/14.
 */
public class VacuumWorldProblem extends Problem {

    public VacuumWorldProblem() {
        super();
        initStates();
        initTransitions();
    }

    private void initStates() {
        for(int i = 1; i<=8; i++) {
            this.addState(new State(i));
        }

        this.addGoalState(new State(7));
        this.addGoalState(new State(8));
    }

    private void initTransitions() {
        Action left = new Action("LEFT");
        Action right = new Action("RIGHT");
        Action suck = new Action("SUCK");

        this.addTransition(1, right, 2);
        this.addTransition(1, suck, 5);
        this.addTransition(1, left, 1);

        this.addTransition(2, left, 1);
        this.addTransition(2, suck, 4);
        this.addTransition(2, right, 2);

        this.addTransition(3, right, 4);
        this.addTransition(3, suck, 7);
        this.addTransition(3, left, 3);

        this.addTransition(4, left, 3);
        this.addTransition(4, right, 4);
        this.addTransition(4, suck, 4);

        this.addTransition(5, right, 6);
        this.addTransition(5, left, 5);
        this.addTransition(5, suck, 5);

        this.addTransition(6, left, 5);
        this.addTransition(6, suck, 8);
        this.addTransition(6, right, 6);

        this.addTransition(7, right, 8);
        this.addTransition(7, left, 7);
        this.addTransition(7, suck, 7);

        this.addTransition(8, left, 7);
        this.addTransition(8, right, 8);
        this.addTransition(8, suck, 8);
    }

    private void addTransition(int s1, Action a, int s2) {
        this.addActionResult(new State(s1), a, new State(s2));
    }

}
