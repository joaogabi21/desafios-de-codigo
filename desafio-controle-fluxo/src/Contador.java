import java.util.Locale;
import java.util.Scanner;

public class Contador {
    public static void main(String[] args) {
        Scanner terminal = new Scanner(System.in).useLocale(Locale.US);
        int parametroUm, parametroDois;

        System.out.print("Digite o primeiro número: ");
        parametroUm = terminal.nextInt();
        System.out.print("Digite o segundo número: ");
        parametroDois = terminal.nextInt();

        try {
            contar (parametroUm,parametroDois);
        } catch (ParametrosInvalidosException e) {
            System.out.print("O segundo parametro deve ser maior que o primeiro.");
        }

    }

    static void contar (int parametroUm, int parametroDois) throws ParametrosInvalidosException {
        if (parametroUm > parametroDois)
            throw new ParametrosInvalidosException();

        int contagem = parametroDois - parametroUm;
        for (int i = 0; i < contagem; i++) 
            System.out.print("Imprimindo o numero " + (i+1) + ".\n");
    }
}
