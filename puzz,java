import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Collections;
import java.util.ArrayList;

public class SlidingPuzzle extends JFrame implements ActionListener {
    private final int GRID_SIZE = 3;
    private JButton[][] buttons;
    private ArrayList<Integer> numbers;
    private int emptyX, emptyY;
    
    public SlidingPuzzle() {
        setTitle("Sliding Puzzle Game");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(GRID_SIZE, GRID_SIZE));
        
        buttons = new JButton[GRID_SIZE][GRID_SIZE];
        numbers = new ArrayList<>();
        
        for (int i = 0; i < GRID_SIZE * GRID_SIZE - 1; i++) {
            numbers.add(i + 1);
        }
        numbers.add(0); // Empty tile
        Collections.shuffle(numbers);
        
        int index = 0;
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                int value = numbers.get(index++);
                buttons[i][j] = new JButton(value == 0 ? "" : String.valueOf(value));
                buttons[i][j].setFont(new Font("Arial", Font.BOLD, 24));
                buttons[i][j].addActionListener(this);
                add(buttons[i][j]);
                if (value == 0) {
                    emptyX = i;
                    emptyY = j;
                }
            }
        }
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        JButton clicked = (JButton) e.getSource();
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                if (buttons[i][j] == clicked) {
                    if ((Math.abs(emptyX - i) == 1 && emptyY == j) ||
                        (Math.abs(emptyY - j) == 1 && emptyX == i)) {
                        buttons[emptyX][emptyY].setText(clicked.getText());
                        clicked.setText("");
                        emptyX = i;
                        emptyY = j;
                        checkWin();
                    }
                    return;
                }
            }
        }
    }
    
    private void checkWin() {
        int num = 1;
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                String text = buttons[i][j].getText();
                if (!text.isEmpty() && Integer.parseInt(text) != num++) {
                    return;
                }
            }
        }
        JOptionPane.showMessageDialog(this, "Congratulations! You solved the puzzle!");
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new SlidingPuzzle().setVisible(true);
        });
    }
}
