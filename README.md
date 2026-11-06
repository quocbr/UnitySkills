# Unity Skills Workbench

Dự án Unity 6 cung cấp **một skill duy nhất, `$unity-skills`**, kết hợp hướng dẫn chính thức của Unity với công cụ thao tác trực tiếp trong Editor của Besty. [Danh mục quy trình hợp nhất](unity-skills/references/workflows.md) gom các chức năng giao nhau như UI Toolkit, uGUI, CLI, UPM, NavMesh, vật lý, hậu kỳ và Shader Graph. Các chức năng riêng vẫn có tài liệu bên trong skill.

## Bắt đầu

1. Trong Unity Hub, chọn **Add project from disk** và mở thư mục này với Unity **6000.3.8f1**. Unity Package Manager sẽ nạp Besty từ mã nguồn trong dự án. Lần mở đầu có thể cần mạng để tải các package phụ thuộc từ registry của Unity.
2. Từ thư mục gốc, chạy lệnh sau với Python 3, rồi mở lại workspace trong Codex để nạp skills.

   ```powershell
   python scripts/install_skills.py --agent codex
   ```

   Dùng `--agent claude-code` cho Claude Code. Nếu đã cài bản tách rời, thêm `--migrate` để sao lưu các bản nhận diện được ra ngoài thư mục agent quét và thay bằng skill hợp nhất. Nếu muốn dùng Python client của Besty, cài `requests` trong môi trường Python của agent bằng `python -m pip install requests`.
3. Trong Unity, mở **Window > UnitySkills**, bật máy chủ và ghi lại cổng hiện trong bảng điều khiển. Ví dụ, nếu cổng là `8090`, kiểm tra bằng lệnh sau.

   ```powershell
   curl.exe http://localhost:8090/health
   ```

   Dùng đúng cổng của dự án nếu đang mở nhiều Editor. Khi yêu cầu agent ghi vào Editor, Besty kiểm tra instance đích và áp dụng chế độ quyền trong bảng UnitySkills.

UnitySkills dùng tiếng Việt mặc định khi chưa có tùy chọn ngôn ngữ đã lưu. Nếu đang dùng ngôn ngữ khác, mở **Settings > Pinned languages**, chọn **Vietnamese**, rồi bấm **VI** ở chân cửa sổ. Tên kỹ thuật Unity, tên tab như **AI Config**, và tên skill trong API giữ nguyên để dễ đối chiếu với Editor và tài liệu.

Thử yêu cầu trong Codex bằng `$unity-skills kiểm tra UI Toolkit của scene đang mở và đề xuất nơi gắn UIDocument cho HUD`. Skill sẽ dùng cùng một quy trình để xem cấu trúc UI, truy vấn Editor khi cần và kiểm tra cấu hình hiện có.

Trong Workbench, **Window > UnitySkills > AI Config** cũng đọc mẫu hợp nhất tại `unity-skills/`. Khi chuyển từ bản cũ, dùng script với `--migrate` để sao lưu trước khi cài.

## Dùng với một dự án Unity khác

Trong Unity của dự án đích, chọn **Package Manager → + → Install package from Git URL** và dán URL sau.

```text
https://github.com/quocbr/UnitySkills.git?path=/upstream/besty-unity-skills/SkillsForUnity#main
```

Mở **Window → UnitySkills → AI Config → Codex**, chọn **Cài đặt (Project)** hoặc **Cài đặt (Global)**. Gói đi kèm đúng mẫu `$unity-skills` hợp nhất và giao diện tiếng Việt. Bật **Khởi động Server** khi cần làm việc trực tiếp với Editor. Nếu đã cài skill hợp nhất ở chế độ Global, mở project trong Codex để sử dụng.

Cập nhật gói Git qua **Package Manager** để tiếp tục nhận đúng bản Workbench. Nếu đã tải repo về máy, cũng có thể chọn **Install package from disk** và trỏ đến [package.json](upstream/besty-unity-skills/SkillsForUnity/package.json).

## Mã nguồn và giấy phép

| Thành phần | Bản nguồn đã ghim | Giấy phép |
| --- | --- | --- |
| [Skills chính thức](upstream/unity-technologies-skills/skills) | [`ba28c24`](https://github.com/Unity-Technologies/skills/tree/ba28c24fc7e569fa0fd5b6bf16ab2bb0acef0594) | [Unity Companion License](upstream/unity-technologies-skills/LICENSE.md) |
| [Gói Besty và Python client](upstream/besty-unity-skills/SkillsForUnity) | [`a2d4135`](https://github.com/Besty0728/Unity-Skills/tree/a2d413571ea32084fa17a56ba9c9341831df4f4c), v2.9.1 | [MIT](upstream/besty-unity-skills/LICENSE) |

Mẫu `unity-skills/` giữ cả hai giấy phép. Unity Companion License áp dụng cho phần của Unity Technologies khi dùng với dự án phụ thuộc Unity. [Điều khoản Unity Companion License](https://unity.com/legal/licenses/unity-companion-license).
