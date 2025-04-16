package gsu.crypt.quiz4_1;

import static gsu.crypt.util.Utils.*;

import gsu.crypt.quiz3_3.VigenereCipher;
import java.util.Scanner;

public class UnbreakableCipher {
	
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Enter text : ");
		String text = scanner.nextLine();
		
		String key = getKey(text.length());
		
		System.out.println("Enter Key : " + key);
		String encryptedText = VigenereCipher.encryptText(text, key);
		
		System.out.println("Encrypted text : " + encryptedText);
		
		scanner.close();
	}

	private static String getKey(int size) {
		StringBuffer buffer = new StringBuffer();
		
		int length = ALPHABET.length();
		
		for(int i = 0; i<size; ++i) {
			int index = (int) (Math.random() * length);
			String character = ALPHABET.substring(index, index + 1);
			buffer.append(character);
		}
		
		return buffer.toString();
	}
	
}