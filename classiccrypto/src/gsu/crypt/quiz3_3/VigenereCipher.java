package gsu.crypt.quiz3_3;

import static gsu.crypt.util.Utils.*;

import java.util.Scanner;

public class VigenereCipher {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter key : ");
		String key = scanner.nextLine();
		
		System.out.print("Enter plain text : ");
		String text = scanner.nextLine();
		
		String encryptedText = encryptText(text, key);
			
		System.out.println(encryptedText);
		
		scanner.close();
	}

	public static String encryptText(String text, String key) {
		int keyLength = key.length();
		int textLength = text.length();
		StringBuffer buffer = new StringBuffer();
		
		for(int i = 0; i<textLength; ++i) {
			int keyIndex = i % keyLength;
			String keyLetter = key.substring(keyIndex, keyIndex + 1);
			String textLetter = text.substring(i, i+1);
			
			int row = ALPHABET.indexOf(keyLetter);
			int column = LOWCASE_ALPHABET.indexOf(textLetter);
			
			int encIndex = (row + column) % ALPHABET.length();
			String encLetter = ALPHABET.substring(encIndex, encIndex + 1);
			buffer.append(encLetter);
		}
		return buffer.toString();
	}
}
