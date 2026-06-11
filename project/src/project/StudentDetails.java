package project;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class StudentDetails extends JFrame {

    JTextField nameField;
    JTextField phoneField;

    JComboBox<String> genderBox;

    public void newPage() {

        setTitle(
                "Student Details"
        );

        setSize(
                500,
                500
        );

        setLayout(null);

        // Name
        JLabel nameLabel =
                new JLabel(
                        "Name"
                );

        nameLabel.setBounds(
                50, 50, 100, 30
        );

        add(nameLabel);

        nameField =
                new JTextField();

        nameField.setBounds(
                180, 50, 200, 30
        );

        add(nameField);

        // Gender
        JLabel genderLabel =
                new JLabel(
                        "Gender"
                );

        genderLabel.setBounds(
                50, 120, 100, 30
        );

        add(genderLabel);

        String genders[] =
                {"Male", "Female"};

        genderBox =
                new JComboBox<>(
                        genders
                );

        genderBox.setBounds(
                180, 120, 200, 30
        );

        add(genderBox);

        // Phone
        JLabel phoneLabel =
                new JLabel(
                        "Phone"
                );

        phoneLabel.setBounds(
                50, 190, 100, 30
        );

        add(phoneLabel);

        phoneField =
                new JTextField();

        phoneField.setBounds(
                180, 190, 200, 30
        );

        add(phoneField);

        // Download Button
        JButton downloadBtn =
                new JButton(
                        "Download Certificate"
                );

        downloadBtn.setBounds(
                120, 300, 250, 50
        );

        add(downloadBtn);

        // Button Action
        downloadBtn
                .addActionListener(
                        new ActionListener() {

            public void actionPerformed(
                    ActionEvent e) {

                String name =
                        nameField
                                .getText();

                String gender =
                        genderBox
                                .getSelectedItem()
                                .toString();

                String phone =
                        phoneField
                                .getText();

                CertificateGenerator
                        .generateCertificate(

                                name,
                                gender,
                                phone,
                                ScoreManager.totalMarks
                        );
            }
        });

        setVisible(true);
    }
}