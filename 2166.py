import sys
import math
from typing import List, Tuple, Optional

Point = Tuple[float, float]

def find_centroid(points: List[Point]) -> Point:
    n = len(points)
    if n == 0:
        raise ValueError("빈 좌표 리스트입니다.")
    cx = sum(x for x, _ in points) / n
    cy = sum(y for _, y in points) / n
    return (cx, cy)

def sort_clockwise(points: List[Point], centroid: Optional[Point] = None) -> List[Point]:
    """
    중심점을 기준으로 각도를 계산해 시계 방향으로 정렬합니다.
    같은 각도일 때는 중심에서 가까운 점이 먼저 오도록 합니다.
    """
    if len(points) < 2:
        return points[:]
    cx, cy = centroid if centroid is not None else find_centroid(points)

    def angle(p: Point) -> float:
        return math.atan2(p[1] - cy, p[0] - cx)  # -π ~ π (CCW 기준)

    def radius(p: Point) -> float:
        return math.hypot(p[0] - cx, p[1] - cy)

    ccw_sorted = sorted(points, key=lambda p: (angle(p), radius(p)))
    cw_sorted = list(reversed(ccw_sorted))
    return cw_sorted

def polygon_area(points: List[Point]) -> float:
    """
    Shoelace formula로 면적을 계산합니다. (절댓값 반환)
    points는 다각형의 경계 순서(시계/반시계)대로 주어져야 합니다.
    """
    n = len(points)
    s = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0

def main():
    input = sys.stdin.readline
    N = int(input().strip())
    pts: List[Point] = []
    for _ in range(N):
        x, y = map(int, input().split())
        pts.append((x, y))

    # 기본: 입력이 이미 "다각형을 이루는 순서"이므로 정렬 없이 바로 계산
    USE_SORT = False  # 필요시 True로 변경하면 시계방향 정렬 후 면적 계산

    if USE_SORT:
        c = find_centroid(pts)
        pts = sort_clockwise(pts, c)

    area = polygon_area(pts)
    # 소수점 첫째 자리까지 출력 (둘째 자리에서 반올림)
    print(f"{area:.1f}")

if __name__ == "__main__":
    main()
