package gsu.crypt.vigenere.decrypt;

import static gsu.crypt.util.Utils.*;

import java.util.Scanner;

public class VigenereCipherDecryptor {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter key : ");
		String key = scanner.nextLine();
		
		System.out.print("Enter encrypted text : ");
		String text = scanner.nextLine();
		
		String decryptedText = getDecryptedText(text, key);
		
		System.out.println(decryptedText);
		
		scanner.close();
	}

	public static String getDecryptedText(String text, String key) {
		StringBuffer result = new StringBuffer();
		int textLength = text.length();
		int keyLength = key.length();
		int alphabetLength = ALPHABET.length();
		
		int [] alphabetIndexesOfKey = new int[keyLength];
		for(int i = 0; i<alphabetIndexesOfKey.length; ++i) {
			String letter = key.substring(i, i + 1);
			alphabetIndexesOfKey[i] = ALPHABET.indexOf(letter);
		}
		
		for(int i = 0; i<textLength; ++i) {
			String letter = text.substring(i, i + 1);
			int index = ALPHABET.indexOf(letter);
			
			int keyIndex = i % keyLength;
			
			int originalIndex = (index - alphabetIndexesOfKey[keyIndex] + alphabetLength) % alphabetLength;
			result.append(LOWCASE_ALPHABET.substring(originalIndex, originalIndex + 1));
		}
		
		return result.toString();
	}
	
	public static String getDecryptedText(String text, int [] alphabetIndexesOfKey, char [] key, char [] result) {
		int textLength = text.length();
		int alphabetLength = ALPHABET.length();
		
		for(int i = 0; i<textLength; ++i) {
			String letter = text.substring(i, i + 1);
			int index = ALPHABET.indexOf(letter);
			
			int keyIndex = i % key.length;
			
			int originalIndex = (index - alphabetIndexesOfKey[keyIndex] + alphabetLength) % alphabetLength;
			result[i] = LOWCASE_ALPHABET.charAt(originalIndex);
		}
		
		return new String(result);
	}
}
