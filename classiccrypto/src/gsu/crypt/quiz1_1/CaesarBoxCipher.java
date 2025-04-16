package gsu.crypt.quiz1_1;

import java.util.Scanner;

public class CaesarBoxCipher {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("Enter plain text : ");
		String content = scanner.nextLine();
		
		String encryptedText = encryptText(content);
		
		System.out.println("Result : " + encryptedText);
		
		scanner.close();
	}

	private static String encryptText(String content) {
		String result;
		if(content == null || content.trim().length() == 0) {
			result = null;
		} else {
			int length = getColumnLength(content);
			result = encryptTextWithColLength(content, length);
		}
		
		return result;
	}

	private static String encryptTextWithColLength(String content, int length) {
		StringBuffer buffer = new StringBuffer();
		int contentLength = content.length();
		
		for(int i = 0; i<length; ++i) {
			for(int j = 0; j<length; ++j) {
				int index = j * length + i;
				if(index < contentLength)
					buffer.append(content.substring(index, index + 1));
			}
		}
		
		return buffer.toString();
	}

	private static int getColumnLength(String content) {
		int length = content.length();
		int sqrt = (int) Math.sqrt(length);
		
		return sqrt * sqrt == length ? sqrt : sqrt + 1;
	}
}
