from manim import *
import numpy as np
from manim_slides import Slide

class Final1_1(Slide):
    def construct(self):
        np.random.seed(42)
        # ==========================================================
        # Slajd 1: Tytuł
        # ==========================================================
        title = Text("Principal Component Analysis - PCA", font_size=48, weight=BOLD)
        authors = Text("Mariusz Godlewski, Piotr Kędzierski", font_size=32)
        authors.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(FadeIn(authors, shift=UP))
        
        self.next_slide()
        self.clear()
        # -----------------------------
        # 1. RAW DATA
        # -----------------------------
        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 10, 1],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": True},
        ).to_edge(DOWN)

        title = Tex("Raw Dataset (Different Scales)", font_size=42).to_edge(UP)

        mean = [50, 5]
        cov = [[400, 30], [30, 3]]
        points = np.random.multivariate_normal(mean, cov, 40)

        dots = VGroup(*[
            Dot(axes.c2p(x, y), radius=0.05, color=GREEN)
            for x, y in points
        ])

        self.play(Create(axes), Write(title))
        self.play(LaggedStartMap(FadeIn, dots, lag_ratio=0.05))
        
        self.next_slide()

        # -----------------------------
        # 2. NORMALIZATION
        # -----------------------------
        title_norm = Tex("Normalization (0–1)", font_size=42).to_edge(UP)

        min_vals = points.min(axis=0)
        max_vals = points.max(axis=0)
        normalized = (points - min_vals) / (max_vals - min_vals)

        axes_norm = Axes(
            x_range=[0, 1, 0.2],
            y_range=[0, 1, 0.2],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": True},
        ).to_edge(DOWN)

        norm_dots = VGroup(*[
            Dot(axes_norm.c2p(x, y), radius=0.05, color=BLUE)
            for x, y in normalized
        ])

        self.play(
            Transform(axes, axes_norm),
            Transform(dots, norm_dots),
            Transform(title, title_norm),
            run_time=2
        )
        
        self.next_slide()

        # -----------------------------
        # 3. CENTERING
        # -----------------------------
        title_center = Tex("Centering (Subtract Mean)", font_size=42).to_edge(UP)

        mean_point = np.mean(normalized, axis=0)
        centered = normalized - mean_point

        axes_center = Axes(
            x_range=[-0.5, 0.5, 0.2],
            y_range=[-0.5, 0.5, 0.2],
            x_length=10,
            y_length=5,
            axis_config={"include_numbers": True},
        ).to_edge(DOWN)

        centered_dots = VGroup(*[
            Dot(axes_center.c2p(x, y), radius=0.05, color=GREEN)
            for x, y in centered
        ])

        mean_dot = Dot(axes_center.c2p(0, 0), color=RED)

        self.play(Transform(title, title_center))
        self.play(FadeIn(mean_dot))
        
        self.next_slide()
        
        self.play(
            Transform(axes, axes_center),
            Transform(dots, centered_dots),
            FadeOut(mean_dot),
            run_time=2
        )
        
        self.next_slide()

        # -----------------------------
        # 4. VARIANCE
        # -----------------------------
        title_var = Tex("Variance (Distance from Mean)", font_size=42).to_edge(UP)
        self.play(Transform(title, title_var))

        sample_dots = dots[:4]

        lines = VGroup()
        for dot in sample_dots:
            x, y = axes_center.p2c(dot.get_center())
            lines.add(
                Line(dot.get_center(), axes_center.c2p(x, 0), color=YELLOW)
            )

        self.play(Create(lines), run_time=2)
        
        self.next_slide()

        # -----------------------------
        # 5. COVARIANCE
        # -----------------------------
        title_cov = Tex("Covariance: dx $\\times$ dy", font_size=42).to_edge(UP)
        self.play(FadeOut(lines), Transform(title, title_cov))

        rects = VGroup()
        for dot in sample_dots:
            origin_pt = axes_center.c2p(0, 0)
            dot_pt = dot.get_center()

            rect = Rectangle(
                width=abs(dot_pt[0] - origin_pt[0]),
                height=abs(dot_pt[1] - origin_pt[1]),
                color=ORANGE,
                fill_opacity=0.3
            )

            rect.move_to((origin_pt + dot_pt) / 2)
            rects.add(rect)

        self.play(FadeIn(rects), run_time=2)
        
        self.next_slide()

        # -----------------------------
        # 6. COVARIANCE MATRIX
        # -----------------------------
        title_matrix = Tex("Covariance Matrix", font_size=42).to_edge(UP)
        matrix = MathTex(
            r"\begin{bmatrix} \sigma_x^2 & \sigma_{xy} \\ \sigma_{yx} & \sigma_y^2 \end{bmatrix}"
        ).scale(1.2)
        matrix.next_to(title_matrix, DOWN, buff=0.5)

        self.play(
            FadeOut(axes),
            FadeOut(dots),
            FadeOut(rects),
            Transform(title, title_matrix),
            Write(matrix)
        )
        
        self.next_slide()

        # -----------------------------
        # 7. OUTER PRODUCT: x x^T
        # -----------------------------
        title_outer = Tex("Outer Product: $x x^T$", font_size=42).to_edge(UP)

        outer = MathTex(
            r"x x^T =",
            r"\begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}",
            r"\begin{bmatrix} x_1 & x_2 & x_3 \end{bmatrix}",
            r"=",
            r"\begin{bmatrix} x_1^2 & x_1 x_2 & x_1 x_3 \\ x_2 x_1 & x_2^2 & x_2 x_3 \\ x_3 x_1 & x_3 x_2 & x_3^2 \end{bmatrix}"
        ).scale(0.9) 
        outer.next_to(title_outer, DOWN, buff=0.5)

        self.play(
            Transform(title, title_outer),
            Transform(matrix, outer),
            run_time=2
        )
        
        self.next_slide() 


if __name__ == "__main__":
    scene = Final1_1()
    scene.render()