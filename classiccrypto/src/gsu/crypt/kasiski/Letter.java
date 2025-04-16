package gsu.crypt.kasiski;

public class Letter implements Comparable<Letter> {
	private double frequency;
	private String character;

	public String getCharacter() {
		return character;
	}
	public void setCharacter(String character) {
		this.character = character;
	}
	public double getFrequency() {
		return frequency;
	}
	public void setFrequency(double frequency) {
		this.frequency = frequency;
	}
	
	public int compareTo(Letter arg0) {
		int result = 0;
		
		if(arg0 == null || arg0.getFrequency() < getFrequency())
			result = 1;
		else if(arg0.getFrequency() > getFrequency())
			result = -1;
		
		return result;
	}
}
