import java.util.Locale;
import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in).useLocale(Locale.US);

        System.out.print("Por favor, digite o número da Agência:");
        int numero = scanner.nextInt();

        System.out.print("Por favor, digite o nome da Agência:");
        String agencia = scanner.next();

        System.out.print("Por favor, digite o nome do Cliente:");
        String nomeCliente = scanner.next();

        System.out.print("Por favor, digite o saldo da conta:");
        double saldo = scanner.nextDouble();

        System.out.print("Olá " + nomeCliente + ", obrigado por criar uma conta em nosso banco.");
        System.out.print("Sua Agência é " + agencia + ", conta " + numero + " e seu saldo de " + saldo + " já está disponível para saque.");
    }
}
