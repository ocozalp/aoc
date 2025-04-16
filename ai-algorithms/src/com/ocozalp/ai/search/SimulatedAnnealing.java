package com.ocozalp.ai.search;

import com.ocozalp.ai.common.Point;

public class SimulatedAnnealing {

    public static void main(String [] args) {
        Point startingPoint = new Point(1);
        startingPoint.coordinates[0] = 0;

        Point result = simulatedAnnealing(startingPoint, 0.1);

        System.out.println(result.coordinates[0]);
    }

    private static Point simulatedAnnealing(Point startingPoint, double d) {
        Point currentPoint = startingPoint;
        Point child;
        double temperature = 1000.0;
        while(true) {
            temperature = getTemperature(temperature);

            if(temperature <= 1e-6) break;

            child = randomChild(currentPoint, d);

            double diff = evaluate(child) - evaluate(currentPoint);

            if(diff >= 0) currentPoint = child;
            else {
                double prob = Math.pow(Math.E, diff / temperature);
                double randVal = Math.random();
                if(randVal <= prob) currentPoint = child;
            }
        }

        return currentPoint;
    }

    private static double getTemperature(double t) {
        return t * 0.95;
    }

    private static Point randomChild(Point point, double d) {
        double randVal = Math.random();
        Point result = new Point(1);

        if(randVal < 0.5)
            result.coordinates[0] = point.coordinates[0] - d;
        else
            result.coordinates[0] = point.coordinates[0] + d;

        return result;
    }

    private static double evaluate(Point point) {
        double x = point.coordinates[0];

        return (x + 3.0) * (x - 2) * x;
    }
}
