from manim import *
import numpy as np
from sklearn.decomposition import PCA
from manim_slides import Slide

class Final1_4(Slide):
    def construct(self):
        np.random.seed(42)
        # ---------------------------------------------------
        # SLIDE 1: Complexity Equation
        # ---------------------------------------------------
        eq_complexity = MathTex(r"\text{Complexity} = O(", r"n", r"d^2 + d^3)").scale(1.5)
        legend_n = MathTex(r"n = \text{Number of samples}")
        legend_d = MathTex(r"d = \text{Number of features}")
        legend_n.shift(DOWN)
        legend_d.shift(2 * DOWN)

        eq_eigen = MathTex(r"\text{Cov}(X) v= \lambda v")
        eq_eigen.shift(3 * RIGHT)
        eq_complexity.shift(UP)
        self.play(Write(eq_complexity))
        self.play(FadeIn(legend_n), FadeIn(legend_d))

        underline_eq = Underline(eq_complexity[1], color=YELLOW)
        underline = Underline(legend_n, color=YELLOW)

        self.play(
            GrowFromEdge(underline_eq, LEFT),
            GrowFromEdge(underline, LEFT),
            run_time=2,
        )
        
        self.next_slide()

        # ---------------------------------------------------
        # SLIDE 2: Eigenvectors & Eigenvalues Matrices
        # ---------------------------------------------------
        self.play(
            FadeOut(eq_complexity, legend_n, legend_d, underline, underline_eq),
            run_time=1,
        )

        matrix_eigenvectors = Matrix([[4, -2, -3], [4, 5, 2], [7, 8, 9]])
        matrix_eigenvalues = Matrix([[5, 0, 0], [0, 1, 0], [0, 0, 0.2]])

        eigenvectors_title = MathTex(r"\text{Eigenvectors}")
        eigenvalues_title = MathTex(r"\text{Eigenvalues}")

        matrix_eigenvectors.shift(3 * LEFT)
        matrix_eigenvalues.shift(3 * RIGHT)
        eigenvalues_title.next_to(matrix_eigenvalues, UP, buff=1.5)
        eigenvectors_title.next_to(matrix_eigenvectors, UP, buff=1.5)
        ul_eigenvectors = Underline(eigenvectors_title, color=WHITE)
        ul_eigenvalues = Underline(eigenvalues_title, color=WHITE)

        self.play(
            Write(matrix_eigenvectors), FadeIn(eigenvectors_title, ul_eigenvectors)
        )
        self.play(Write(matrix_eigenvalues), FadeIn(eigenvalues_title, ul_eigenvalues))

        rect = SurroundingRectangle(matrix_eigenvalues.get_columns()[0], color=YELLOW)
        rect_tg = SurroundingRectangle(matrix_eigenvalues.get_columns()[1], color=YELLOW)

        self.play(Create(rect))
        self.play(Transform(rect, rect_tg))
        
        rect_tg = SurroundingRectangle(matrix_eigenvalues.get_columns()[2], color=YELLOW)
        self.play(Transform(rect, rect_tg))

        self.next_slide()

        # ---------------------------------------------------
        # SLIDE 3: Non-linear Data Intro & Plot
        # ---------------------------------------------------
        self.play(
            FadeOut(
                rect,
                eigenvalues_title,
                ul_eigenvalues,
                matrix_eigenvalues,
                eigenvectors_title,
                ul_eigenvectors,
                matrix_eigenvectors,
            ),
            run_time=2,
        )

        txt_nonlinear = Tex("Non-linear data")
        self.play(Write(txt_nonlinear.scale(1.5)))

        axes = Axes(
            x_range=[0, 1, 0.5],
            y_range=[0, 1, 0.5],
            x_length=6,
            y_length=6,
            axis_config={
                "color": WHITE,
                "include_numbers": True,
                "include_tip": False,
                "font_size": 18,
            },
        ).move_to(UP * 0.5)

        self.play(LaggedStart(FadeOut(txt_nonlinear), FadeIn(axes), lag_ratio=0.5), run_time=1)

        data = np.loadtxt("data/spiral.csv", delimiter=",")
        labels = np.loadtxt("data/spiral_labels.csv", delimiter=",")

        dots_class_0 = VGroup(
            *[
                Dot(point=axes.c2p(x, y), radius=0.03, color=BLUE, fill_opacity=0.4)
                for (x, y), label in zip(data, labels)
                if label == 0
            ]
        )

        dots_class_1 = VGroup(
            *[
                Dot(point=axes.c2p(x, y), radius=0.03, color=RED, fill_opacity=0.4)
                for (x, y), label in zip(data, labels)
                if label == 1
            ]
        )

        self.play(
            LaggedStartMap(Create, dots_class_0, lag_ratio=0.01),
            LaggedStartMap(Create, dots_class_1, lag_ratio=0.01),
            run_time=2,
        )

        self.next_slide()

        # ---------------------------------------------------
        # SLIDE 4: PCA Projection
        # ---------------------------------------------------
        pca = PCA(n_components=1)
        data_pca = pca.fit_transform(data)

        eigenvector = pca.components_[0]
        mean = [0.5, 0.5]

        vector1 = Arrow(
            start=axes.c2p(*mean),
            end=axes.c2p(*(mean + eigenvector / 5)),
            buff=0,
            color=WHITE,
            stroke_width=8,
            max_stroke_width_to_length_ratio=10,
            z_index=1,
        )

        self.play(GrowArrow(vector1), run_time=1)

        projections = [
            np.dot(eigenvector, np.array([x, y]) - mean) * eigenvector + mean
            for x, y in data
        ]

        proj_dots_class_0 = VGroup(
            *[
                Dot(point=axes.c2p(x, y), radius=0.03, color=BLUE, fill_opacity=0.4)
                for (x, y), label in zip(projections, labels)
                if label == 0
            ]
        )

        proj_dots_class_1 = VGroup(
            *[
                Dot(point=axes.c2p(x, y), radius=0.03, color=RED, fill_opacity=0.4)
                for (x, y), label in zip(projections, labels)
                if label == 1
            ]
        )

        dots_class_0_original = dots_class_0.copy()
        dots_class_1_original = dots_class_1.copy()

        self.play(
            Transform(dots_class_0, proj_dots_class_0),
            Transform(dots_class_1, proj_dots_class_1),
            run_time=2,
        )

        self.next_slide()

        # ---------------------------------------------------
        # SLIDE 5: Arbitrary Vector Projection
        # ---------------------------------------------------
        self.play(
            Transform(dots_class_0, dots_class_0_original),
            Transform(dots_class_1, dots_class_1_original),
            run_time=2,
        )

        eigenvector2 = np.array([0.2, -0.5])
        eigenvector2 /= np.linalg.norm(eigenvector2)
        mean2 = [0.5, 0.5]

        vector2 = Arrow(
            start=axes.c2p(*mean2),
            end=axes.c2p(*(mean2 + eigenvector2 / 5)),
            buff=0,
            color=WHITE,
            stroke_width=8,
            max_stroke_width_to_length_ratio=10,
            z_index=1,
        )

        self.play(GrowArrow(vector2), FadeOut(vector1), run_time=1)

        projections2 = [
            np.dot(eigenvector2, np.array([x, y]) - mean2) * eigenvector2 + mean2
            for x, y in data
        ]

        proj_dots_class_0_2 = VGroup(
            *[
                Dot(point=axes.c2p(x, y), radius=0.03, color=BLUE, fill_opacity=0.4)
                for (x, y), label in zip(projections2, labels)
                if label == 0
            ]
        )

        proj_dots_class_1_2 = VGroup(
            *[
                Dot(point=axes.c2p(x, y), radius=0.03, color=RED, fill_opacity=0.4)
                for (x, y), label in zip(projections2, labels)
                if label == 1
            ]
        )

        self.play(
            Transform(dots_class_0, proj_dots_class_0_2),
            Transform(dots_class_1, proj_dots_class_1_2),
            run_time=2,
        )

        self.next_slide()


if __name__ == "__main__":
    scene = Final1_4()
    scene.render()