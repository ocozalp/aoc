package com.ocozalp.ai.search;

import com.ocozalp.ai.common.Point;

import java.util.ArrayList;

/**
 *
 * A simple hill climbing example which tries to find the local maxima
 * of a given function.
 *
 */
public class HillClimbing {

    public static void main(String[] args) {
        Point startingPoint = new Point(1);
        startingPoint.coordinates[0] = 0;

        Point result = hillClimbing(startingPoint, 0.1);

        System.out.println(result.coordinates[0]);
    }

    private static Point hillClimbing(Point startingPoint, double stepSize) {
        Point currentPoint;
        Point maxChild = startingPoint;

        double cost;
        double maxChildCost = evaluate(startingPoint);

        do {
            currentPoint = maxChild;
            cost = maxChildCost;

            ArrayList<Point> children = getChildren(currentPoint, stepSize);

            for(Point child : children) {
                double childCost = evaluate(child);
                if(childCost > maxChildCost) {
                    maxChild = child;
                    maxChildCost = childCost;
                }
            }
        } while(cost < maxChildCost); // may diverge

        return currentPoint;
    }

    private static ArrayList<Point> getChildren(Point point, double stepSize) {
        ArrayList<Point> result = new ArrayList<Point>();
        double [] coordinates = new double[point.dimension];

        System.arraycopy(point.coordinates, 0, coordinates, 0, coordinates.length);

        fillChildrenList(result, coordinates, 0, stepSize, false);

        return result;
    }

    private static void fillChildrenList(ArrayList<Point> childrenList, double coordinates[], int level,
                                         double stepSize, boolean changed) {
        if(level == coordinates.length) {
            if(!changed) return; // unnecessary backtracking cost but whatever...

            Point p = new Point(coordinates.length);
            p.setCoordinates(coordinates);
            childrenList.add(p);
        } else {
            double val = coordinates[level];
            for(int i = -1; i<=1; i++) {
                coordinates[level] = val + i * stepSize;
                fillChildrenList(childrenList, coordinates, level+1, stepSize, changed | (i != 0));
            }
            coordinates[level] = val;
        }
    }

    private static double evaluate(Point point) {
        double x = point.coordinates[0];

        return (x + 3.0) * (x - 2) * x;
    }
}