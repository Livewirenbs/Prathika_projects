
package project;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;

public class Dashboard extends JFrame {

    JTextArea codeBox, outputBox;
    JLabel questionLabel;

    int questionIndex = 0;

    // Questions
    String[] questions = {

            "Write a program to check whether 7 is Prime Number\nOutput should be: Prime",

            "Write a program to check palindrome number (121)\nOutput should be: Palindrome",

            "Write a program to check even or odd (10)\nOutput should be: Even",

            "Write a program to print factorial of 5\nOutput should be: 120",

            "Write a program to reverse number 123\nOutput should be: 321"
    };

    // Correct Answers
    String[] answers = {
            "Prime",
            "Palindrome",
            "Even",
            "120",
            "321"
    };

    public void newpage() {

        setTitle("Cody Hub");
        setSize(1500, 900);
        setLayout(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Heading
        JLabel heading =
                new JLabel("CODY HUB-Basic Level question");

        heading.setBounds(
                600, 10, 800, 40
        );

        heading.setFont(
                new Font("Arial",
                        Font.BOLD, 35)
        );

        add(heading);

        // Question Label
        questionLabel = new JLabel();

        questionLabel.setBounds(
                180, 60, 1200, 100
        );

        questionLabel.setFont(
                new Font("Arial",
                        Font.BOLD, 28)
        );

        updateQuestion();

        add(questionLabel);

        // Code Label
        JLabel codeLabel =
                new JLabel("Write Code");

        codeLabel.setBounds(
                180, 150, 300, 40
        );

        codeLabel.setFont(
                new Font("Arial",
                        Font.BOLD, 26)
        );

        add(codeLabel);

        // Code Text Area
        codeBox = new JTextArea();

        codeBox.setFont(
                new Font("Monospaced",
                        Font.BOLD, 20)
        );

        JScrollPane codeScroll =
                new JScrollPane(codeBox);

        // Left side coding block
        codeScroll.setBounds(
                100, 180, 580, 420
        );

        add(codeScroll);

        // Output Label
        JLabel outputLabel =
                new JLabel("Output");

        outputLabel.setBounds(
                850, 150, 300, 40
        );

        outputLabel.setFont(
                new Font("Arial",
                        Font.BOLD, 26)
        );

        add(outputLabel);

        // Output Text Area
        outputBox = new JTextArea();

        outputBox.setEditable(false);

        outputBox.setFont(
                new Font("Monospaced",
                        Font.BOLD, 20)
        );

        outputBox.setLineWrap(true);
        outputBox.setWrapStyleWord(true);

        JScrollPane outputScroll =
                new JScrollPane(
                        outputBox,
                        JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,
                        JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED
                );

        // Right side output block
        outputScroll.setBounds(
                700, 180, 580, 420
        );

        add(outputScroll);

        // Run Button
        JButton runBtn =
                new JButton("Run Code");

        runBtn.setBounds(
                420, 650, 220, 60
        );

        runBtn.setFont(
                new Font("Arial",
                        Font.BOLD, 24)
        );

        add(runBtn);

        // Next Question Button
        JButton nextBtn =
                new JButton("Next Question");

        nextBtn.setBounds(
                820, 650, 260, 60
        );

        nextBtn.setFont(
                new Font("Arial",
                        Font.BOLD, 24)
        );

        add(nextBtn);

        // Run Button Action
        runBtn.addActionListener(
                new ActionListener() {

            public void actionPerformed(
                    ActionEvent e) {

                runCode();
            }
        });

        // Next Button Action
        nextBtn.addActionListener(
                new ActionListener() {

            public void actionPerformed(
                    ActionEvent e) {

                if (questionIndex
                        < questions.length - 1) {

                    questionIndex++;

                    updateQuestion();

                    // Clear old code and output
                    codeBox.setText("");
                    outputBox.setText("");

                } else {

                    JOptionPane.showMessageDialog(
                            null,
                            "All Questions Completed!"
                    );
                    dispose();
                    inter r=new inter();
                   
                    r.newpage1();
                    
                }
            }
        });

        setVisible(true);
    }

    // Update Question
    public void updateQuestion() {

        questionLabel.setText(
                "<html><center>Question:<br>"
                        + questions[questionIndex]
                        .replace("\n", "<br>")
                        + "</center></html>"
        );
    }
    // Run User Code
    public void runCode() {

        try {

            String userCode =
                    codeBox.getText();

            outputBox.setText("");

            // Save user code
            FileWriter writer =
                    new FileWriter(
                            "UserProgram.java"
                    );

            writer.write(userCode);
            writer.close();

            // Compile program
            Process compile =
                    Runtime.getRuntime()
                            .exec(
                                    "javac UserProgram.java"
                            );

            compile.waitFor();

            // Compile Errors
            BufferedReader compileError =
                    new BufferedReader(
                            new InputStreamReader(
                                    compile.getErrorStream()
                            )
                    );

            String line;
            String errors = "";

            while ((line =
                    compileError.readLine())
                    != null) {

                errors += line + "\n";
            }

            // Show compile errors
            if (!errors.isEmpty()) {

                outputBox.setText(errors);
                return;
            }

            // Run Program
            Process run =
                    Runtime.getRuntime()
                            .exec(
                                    "cmd /c java UserProgram"
                            );

            run.waitFor();

            // Read Output
            BufferedReader reader =
                    new BufferedReader(
                            new InputStreamReader(
                                    run.getInputStream()
                            )
                    );

            String output = "";

            while ((line =
                    reader.readLine())
                    != null) {

                output += line + "\n";
            }

            // Runtime Errors
            BufferedReader runtimeError =
                    new BufferedReader(
                            new InputStreamReader(
                                    run.getErrorStream()
                            )
                    );

            while ((line =
                    runtimeError.readLine())
                    != null) {

                output += line + "\n";
            }

            // Show Output
            outputBox.setText(output);

            // Validate Answer
            if (output.trim().equals(
                    answers[questionIndex]
            )) {

            	ScoreManager.addMark();

            	JOptionPane.showMessageDialog(
            	        this,
            	        "✅ Correct Answer"
            	);
            } else {

                JOptionPane.showMessageDialog(
                        this,
                        "❌ Wrong Answer"
                );
            }

        } catch (Exception ex) {

            outputBox.setText(
                    ex.toString()
            );
        }
    }

    public static void main(String[] args) {

        Dashboard d =
                new Dashboard();

        d.newpage();
    }
}

