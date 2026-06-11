package project;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;

public class hard extends JFrame {

    JTextArea codeBox, outputBox;
    JLabel questionLabel;

    int questionIndex = 0;

    // Hard Level Questions
    String[] questions = {

            "Write a program to find factorial of 5\nOutput should be: 120",

            "Write a program to reverse number 1234\nOutput should be: 4321",

            "Write a program to check whether 29 is Prime Number\nOutput should be: Prime",

            "Write a program to find sum of array 10,20,30,40\nOutput should be: 100",

            "Write a program to find second largest number in array 10,50,30,80,60\nOutput should be: 60"
    };

    // Correct Answers
    String[] answers = {

            "120",
            "4321",
            "Prime",
            "100",
            "60"
    };

    public void newpage2() {

        setTitle("Cody Hub");
        setSize(1500, 900);
        setLayout(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Heading
        JLabel heading =
                new JLabel("CODY HUB - Hard Level");

        heading.setBounds(
                500, 10, 500, 40
        );

        heading.setFont(
                new Font(
                        "Arial",
                        Font.BOLD,
                        35
                )
        );

        add(heading);

        // Question Label
        questionLabel =
                new JLabel();

        questionLabel.setBounds(
                180, 60, 1200, 100
        );

        questionLabel.setFont(
                new Font(
                        "Arial",
                        Font.BOLD,
                        28
                )
        );

        updateQuestion();

        add(questionLabel);

        // Code Label
        JLabel codeLabel =
                new JLabel(
                        "Write Code"
                );

        codeLabel.setBounds(
                180, 150, 300, 40
        );

        codeLabel.setFont(
                new Font(
                        "Arial",
                        Font.BOLD,
                        26
                )
        );

        add(codeLabel);

        // Code Text Area
        codeBox =
                new JTextArea();

        codeBox.setFont(
                new Font(
                        "Monospaced",
                        Font.BOLD,
                        20
                )
        );

        JScrollPane codeScroll =
                new JScrollPane(
                        codeBox
                );

        codeScroll.setBounds(
                100, 180, 580, 420
        );

        add(codeScroll);

        // Output Label
        JLabel outputLabel =
                new JLabel(
                        "Output"
                );

        outputLabel.setBounds(
                850, 150, 300, 40
        );

        outputLabel.setFont(
                new Font(
                        "Arial",
                        Font.BOLD,
                        26
                )
        );

        add(outputLabel);

        // Output Text Area
        outputBox =
                new JTextArea();

        outputBox.setEditable(
                false
        );

        outputBox.setFont(
                new Font(
                        "Monospaced",
                        Font.BOLD,
                        20
                )
        );

        JScrollPane outputScroll =
                new JScrollPane(
                        outputBox
                );

        outputScroll.setBounds(
                700, 180, 580, 420
        );

        add(outputScroll);

        // Run Button
        JButton runBtn =
                new JButton(
                        "Run Code"
                );

        runBtn.setBounds(
                420, 650, 220, 60
        );

        runBtn.setFont(
                new Font(
                        "Arial",
                        Font.BOLD,
                        24
                )
        );

        add(runBtn);

        // Next Question Button
        JButton nextBtn =
                new JButton(
                        "Next Question"
                );

        nextBtn.setBounds(
                820, 650, 260, 60
        );

        nextBtn.setFont(
                new Font(
                        "Arial",
                        Font.BOLD,
                        24
                )
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

                    codeBox.setText("");
                    outputBox.setText("");

                } else {

                    JOptionPane.showMessageDialog(
                            null,
                            "All Questions Completed!"
                    );

                    JOptionPane.showMessageDialog(
                            null,
                            "Your Total Mark is : "
                                    + ScoreManager.totalMarks
                    );

                    // If total mark is 15
                    if (ScoreManager.totalMarks
                            == 1) {

                        dispose();

                        StudentDetails s =
                                new StudentDetails();

                        s.newPage();

                    } else {

                        JOptionPane.showMessageDialog(
                                null,
                                "Certificate Available Only For Full Score!"
                        );

                        dispose();
                    }
                }
            }
        });

        setVisible(true);
    }

    // Update Question
    public void updateQuestion() {

        questionLabel.setText(
                "<html><center>Question:<br>"
                        + questions[
                        questionIndex
                        ].replace(
                                "\n",
                                "<br>"
                        )
                        + "</center></html>"
        );
    }

    // Run User Code
    public void runCode() {

        try {

            String userCode =
                    codeBox.getText();

            outputBox.setText("");

            // Save User Code
            FileWriter writer =
                    new FileWriter(
                            "UserProgram.java"
                    );

            writer.write(
                    userCode
            );

            writer.close();

            // Compile
            Process compile =
                    Runtime.getRuntime()
                            .exec(
                                    "javac UserProgram.java"
                            );

            compile.waitFor();

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

                errors +=
                        line + "\n";
            }

            if (!errors.isEmpty()) {

                outputBox.setText(
                        errors
                );

                return;
            }

            // Run Program
            Process run =
                    Runtime.getRuntime()
                            .exec(
                                    "cmd /c java UserProgram"
                            );

            run.waitFor();

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

                output +=
                        line + "\n";
            }

            outputBox.setText(
                    output
            );

            // Validate Answer
            if (output.trim().equals(
                    answers[
                            questionIndex
                    ]
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

    public static void main(
            String[] args) {

        hard h =
                new hard();

        h.newpage2();
    }
}

