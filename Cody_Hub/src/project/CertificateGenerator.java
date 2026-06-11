package project;

import java.io.FileOutputStream;

import javax.swing.JOptionPane;

import com.itextpdf.text.Document;
import com.itextpdf.text.Paragraph;
import com.itextpdf.text.pdf.PdfWriter;

public class CertificateGenerator {

    public static void generateCertificate(

            String name,
            String gender,
            String phone,
            int mark) {

        try {

            // Save inside project folder
            String fileName =
                    "C:\\Users\\ELCOT\\OneDrive\\Desktop\\Certificate.pdf";

            Document document =
                    new Document();

            PdfWriter.getInstance(
                    document,
                    new FileOutputStream(
                            fileName
                    )
            );

            document.open();

            document.add(
                    new Paragraph(
                            "CODY HUB CERTIFICATE"
                    )
            );

            document.add(
                    new Paragraph(
                            " "
                    )
            );

            document.add(
                    new Paragraph(
                            "Name : "
                                    + name
                    )
            );

            document.add(
                    new Paragraph(
                            "Gender : "
                                    + gender
                    )
            );

            document.add(
                    new Paragraph(
                            "Phone : "
                                    + phone
                    )
            );

            document.add(
                    new Paragraph(
                            "Score : "
                                    + mark
                    )
            );

            document.close();

            JOptionPane.showMessageDialog(
                    null,
                    "PDF Generated!"
            );

        } catch (Exception e) {

            JOptionPane.showMessageDialog(
                    null,
                    e.toString()
            );
        }
    }
}

