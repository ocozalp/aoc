package gsu.crypt.quiz2_1;

import static gsu.crypt.util.Utils.*;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.Vector;

public class HomophonicCipher {
	
	public static void main(String[] args) {
		String fileName = "frequencies.txt";
		int [] countVector = getCountVector(fileName);
		
		printCountVector(countVector);
		
		String [][] encryptedLetters = getEncryptedLetters(countVector);
		
		printEncryptedLettersMatrix(encryptedLetters);
		
		Scanner scan = new Scanner(System.in);
		System.out.print("\n*********\nEnter text : ");
		String textToBeEncrypt = scan.nextLine();
		
		String encryptedText = encryptText(textToBeEncrypt, encryptedLetters);
		
		System.out.println("Encrypted text : " + encryptedText);
		
		scan.close();
	}

	private static String encryptText(String textToBeEncrypt, String[][] encryptedLetters) {
		int textLength = textToBeEncrypt.length();
		StringBuffer buffer = new StringBuffer();
		
		for(int i = 0; i<textLength; ++i) {
			String letter = textToBeEncrypt.substring(i, i+1);
			String randomKey = getRandomValue(encryptedLetters, ALPHABET.indexOf(letter));
			buffer.append(randomKey);
		}
		
		return buffer.toString();
	}

	private static String getRandomValue(String[][] encryptedLetters, int i) {
		int keyCount = encryptedLetters[i].length;
		int index = (int) (Math.random() * keyCount);
		return encryptedLetters[i][index];
	}

	private static void printEncryptedLettersMatrix(String[][] encryptedLetters) {
		for(int i = 0; i<encryptedLetters.length; ++i) {
			System.out.print(ALPHABET.substring(i, i+1) + " = ");
			
			for(int j = 0; j<encryptedLetters[i].length; ++j) {
				System.out.print(encryptedLetters[i][j] + ", ");
			}
			
			System.out.println();
		}
	}

	private static String[][] getEncryptedLetters(int[] countVector) {
		String [][] letterMatrix = new String[countVector.length][];
		Vector<String> controlVector = new Vector<String>();
		
		for(int i = 0; i<countVector.length; ++i) {
			letterMatrix[i] = new String[countVector[i]];
			
			for(int j = 0; j<countVector[i]; ++j) {
				letterMatrix[i][j] = getRandomKey(controlVector);
			}
		}
		return letterMatrix;
	}

	private static String getRandomKey(Vector<String> controlVector) {
		String key;
		do {
			int number = (int) (Math.random() * 1000);
			key = padNumber(number);
		}while(controlVector.contains(key));
		
		controlVector.add(key);
		return key;
	}

	private static String padNumber(int number) {
		String key = String.valueOf(number);
		
		if(number < 100)
			key = "0" + key;
		
		if(number < 10)
			key = "0" + key;
		
		return key;
	}

	private static void printCountVector(int[] countVector) {
		int total = 0;
		for(int i = 0; i<countVector.length; ++i) {
			System.out.println(ALPHABET.substring(i, i+1) + " - " + countVector[i]);
			total += countVector[i];
		}
		
		System.out.println("Total : " + total);
	}

	private static int[] getCountVector(String fileName) {
		int [] frequencies = new int[ALPHABET.length()];
		
		BufferedReader br = null;
		try {
			br = new BufferedReader(new InputStreamReader(new FileInputStream(fileName)));
			String line;
			
			while((line  = br.readLine()) != null) {
				int index = line.indexOf("=");
				String letter = line.substring(0, index);
				double value = Double.parseDouble(line.substring(index + 1));
				int alphabetIndex = ALPHABET.indexOf(letter);
				
				frequencies[alphabetIndex] = (int) value;
				
				if(value - (int) value > 0.5d || frequencies[alphabetIndex] == 0)
					frequencies[alphabetIndex]++;
			}
		} catch (Exception e) {
			e.printStackTrace();
			frequencies = null;
		} finally {
			try {
				br.close();
			} catch (Exception e) {
			}
		}
		
		return frequencies;
	}
}