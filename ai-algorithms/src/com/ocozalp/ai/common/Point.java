package com.ocozalp.ai.common;

public class Point {
    public double[] coordinates;
    public int dimension;

    public Point(int dimension) {
        this.dimension = dimension;
        coordinates = new double[dimension];
    }

    public void setCoordinates(double[] coordinates) {
        System.arraycopy(coordinates, 0, this.coordinates, 0, coordinates.length);
    }
}
