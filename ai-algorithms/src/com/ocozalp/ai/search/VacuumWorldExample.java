package com.ocozalp.ai.search;

import com.ocozalp.ai.common.Action;
import com.ocozalp.ai.common.State;

import java.util.ArrayList;

/**
 * Created by ocozalp on 5/18/14.
 */
public class VacuumWorldExample {

    public static void main(String [] args) {
        VacuumWorldProblem problem = new VacuumWorldProblem();

        AndOrSearchTree tree = new AndOrSearchTree(problem);

        ArrayList<Action> steps = tree.search(new State(1));

        if(steps != null) {
            for(Action action : steps) System.out.println(action.getName());
        } else {
            System.out.println("No Solution!");
        }
    }
}
