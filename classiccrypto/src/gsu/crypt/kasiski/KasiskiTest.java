package gsu.crypt.kasiski;

import static gsu.crypt.util.Utils.*;

import java.util.Arrays;
import java.util.Scanner;

public class KasiskiTest {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter key length : ");
		int keyLength = Integer.parseInt(scanner.nextLine());
		
		System.out.print("Enter encrypted text : ");
		String text = scanner.nextLine();
		
		doFrequencyAnalysis(text, keyLength);
		
		scanner.close();
	}

	private static void doFrequencyAnalysis(String text, int keyLength) {
		int textLength = text.length();
		
		for(int i = 0; i<keyLength; ++i) {
			int index = i;
			int [] letterCounts = new int[ALPHABET.length()];
			int count = 0;
			
			while(index < textLength){
				String letter = text.substring(index, index + 1);
				int alphabetIndex = ALPHABET.indexOf(letter);
				letterCounts[alphabetIndex]++;
				index += keyLength;
				++count;
			}
			
			System.out.println("frequencies for " + (i+1) + ". letter : ");
			printAnalysis(letterCounts, count);
			System.out.println();
		}
	}

	private static void printAnalysis(int[] letterCounts, int count) {
		Letter [] letterArray = new Letter[letterCounts.length];
		
		for(int i = 0; i<letterCounts.length; ++i) {
			Letter letter = new Letter();
			letter.setCharacter(ALPHABET.substring(i, i + 1));
			letter.setFrequency((letterCounts[i] * 100.0d) / count);
			letterArray[i] = letter;
		}

		Arrays.sort(letterArray);
		
		for(int i = letterArray.length - 1; i>=0; --i) {
			System.out.println(letterArray[i].getCharacter() + " = " + letterArray[i].getFrequency());
		}
	}
}