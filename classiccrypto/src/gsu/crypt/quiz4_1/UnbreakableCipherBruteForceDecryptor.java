package gsu.crypt.quiz4_1;

import static gsu.crypt.util.Utils.*;

import gsu.crypt.vigenere.decrypt.VigenereCipherDecryptor;
import java.util.Scanner;

public class UnbreakableCipherBruteForceDecryptor {
	
	private static final int ALPHABET_LAST_INDEX = ALPHABET.length() - 1;
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter first encrypted text : ");
		String encryptedText1 = scanner.nextLine();
		
		System.out.print("Enter second encrypted text : ");
		String encryptedText2 = scanner.nextLine();
		
		decryptText(encryptedText1, encryptedText2);
		
		scanner.close();
	}

	private static void decryptText(String encryptedText1, String encryptedText2) {
		int textLength = encryptedText1.length();
		int [] indexes = new int[textLength];
		char text [] = new char[textLength];
		char key [] = new char[textLength];
		
		while(!isFinished(indexes)) {
			String keyStr = generateKeyFromIndexes(indexes, key);
			String decryptedText1 = VigenereCipherDecryptor.getDecryptedText(encryptedText1, indexes, key, text);
			String decryptedText2 = VigenereCipherDecryptor.getDecryptedText(encryptedText2, indexes, key, text);
			System.out.println(keyStr + " : \n" + decryptedText1 + "\n" + decryptedText2);
			
			incrementIndexes(indexes);
		}
	}

	private static void incrementIndexes(int[] indexes) {
		boolean overflow = true;
		for(int i = indexes.length - 1; i>=0 && overflow; --i) {
			if(overflow = indexes[i] == ALPHABET_LAST_INDEX) {
				indexes[i] = 0;
			} else {
				indexes[i]++;
			}
		}
	}

	private static String generateKeyFromIndexes(int[] indexes, char [] key) {
		for(int i = 0; i<indexes.length; ++i) {
			key[i] = ALPHABET.charAt(indexes[i]);
		}
		return new String(key);
	}

	private static boolean isFinished(int[] indexes) {
		boolean result = true;
		for(int i = 0; i<indexes.length && result; ++i) {
			result = indexes[i] == ALPHABET_LAST_INDEX;
		}
		return result;
	}
}
