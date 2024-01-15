import java.io.*;
import hex.genmodel.easy.RowData;
import hex.genmodel.easy.EasyPredictModelWrapper;
import hex.genmodel.easy.prediction.*;
import hex.genmodel.MojoModel;

public class PredictGender {
    public static void main(String[] args) throws Exception {
        EasyPredictModelWrapper model = new EasyPredictModelWrapper(
                MojoModel.load("../build/GLM_model_python_1705310628808_1.zip"));

        RowData row = new RowData();
        row.put("ORG_CODE", "GOVTN");
        row.put("PINCODE", "629702");

        MultinomialModelPrediction p = model.predictMultinomial(row);
        System.out.println("Class probabilities: ");
        for (int i = 0; i < p.classProbabilities.length; i++) {
            if (i > 0) {
                System.out.print(",");
            }
            System.out.print(p.classProbabilities[i]);
        }
        System.out.println("");
    }
}