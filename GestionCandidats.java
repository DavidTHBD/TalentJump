import java.util.*;

public class GestionCandidats {

    static Scanner scanner = new Scanner(System.in);
    static ArrayList<String[]> candidats = new ArrayList<>();

    public static void main(String[] args) {
        int choix;
        do {
            // Affichage du menu
            System.out.println("\n--- MENU ---");
            System.out.println("1. Ajouter un candidat");
            System.out.println("2. Supprimer un candidat par nom");
            System.out.println("3. Modifier un candidat");
            System.out.println("4. Afficher tous les candidats");
            System.out.println("5. Trier les candidats par nom");
            System.out.println("0. Quitter");
            System.out.print("Choix : ");
            choix = scanner.nextInt();
            scanner.nextLine(); 

            switch (choix) {
                case 1 -> ajouterCandidat();
                case 2 -> supprimerCandidat();
                case 3 -> modifierCandidat();
                case 4 -> afficherCandidats();
                case 5 -> trierCandidats();
                case 0 -> System.out.println("Au revoir !");
                default -> System.out.println("Choix invalide.");
            }
        } while (choix != 0);
    }

    static void ajouterCandidat() {
        System.out.print("Nom : ");
        String nom = scanner.nextLine();
        System.out.print("Prénom : ");
        String prenom = scanner.nextLine();
        System.out.print("Age : ");
        String Age = scanner.nextLine();
        System.out.print("Poste_vise : ");
        String Poste_vise = scanner.nextLine();
        System.out.print("Cv : ");
        String Cv = scanner.nextLine();
        System.out.print("Email : ");
        String email = scanner.nextLine();
        candidats.add(new String[]{nom, prenom, Age, Poste_vise, Cv, email});
        System.out.println("Candidat ajouté.");
    }

    static void supprimerCandidat() {
        System.out.print("Nom du candidat à supprimer : ");
        String nom = scanner.nextLine();
        boolean supprimé = candidats.removeIf(c -> c[0].equalsIgnoreCase(nom));
        System.out.println(supprimé ? "Candidat supprimé." : "Candidat non trouvé.");
    }
 
    static void modifierCandidat() {
        System.out.print("Nom du candidat à modifier : ");
        String nom = scanner.nextLine();
        for (String[] c : candidats) {
            if (c[0].equalsIgnoreCase(nom)) {
                System.out.print("Nouveau prénom : ");
                c[1] = scanner.nextLine();
                System.out.print("Nouvel email : ");
                c[2] = scanner.nextLine();
                System.out.println("Candidat modifié.");
                return;
            }
        }
        System.out.println("Candidat non trouvé.");
    }

    static void afficherCandidats() {
        System.out.println("\n--- Liste des candidats ---");
        for (String[] c : candidats) {
            System.out.println("Nom: " + c[0] + ", Prénom: " + c[1] + ", Age: " + c[2] + ", Poste visé:" + c[3] + ", Cv:" + c[4] + ", E-mail :" + c[5]);
        }
    }

    static void trierCandidats() {
        candidats.sort(Comparator.comparing(c -> c[0].toLowerCase()));
        System.out.println("Candidats triés par nom.");
    }

}